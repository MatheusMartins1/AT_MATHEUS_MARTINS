(function ($) {

  "use strict";
  var dados = [];
  dados.add(document.getElementById("inputH").value);
  dados = JSON.parse([dados])
  
  console.log("dado:" + dados)

  // set the dimensions and margins of the graph
  const margin = { top: 10, right: 30, bottom: 20, left: 50 },
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;


  // append the svg object to the body of the page
  const svg = d3.select("#cpu_dataviz")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);


  // Parse the Data
  d3.json(dados).then(function (base) {

    // List of subgroups = header of the csv files = soil condition here
    const subgroups = base.columns.slice(1)

    // List of groups = species here = value of the first column called group -> I show them on the X axis
    const groups = base.map(d => d.group)

    // Add X axis
    const x = d3.scaleBand()
      .domain(groups)
      .range([0, width])
      .padding([0.2])
    svg.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(d3.axisBottom(x).tickSizeOuter(0));

    // Add Y axis
    const y = d3.scaleLinear()
      .domain([0, 100])
      .range([height, 0]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // color palette = one color per subgroup
    const color = d3.scaleOrdinal()
      .domain(subgroups)
      .range(['#e41a1c', '#377eb8'])

    // Normalize the base -> sum of each group must be 100!
    var dataNormalized = []
    base.forEach(function (d) {
      // Compute the total
      var tot = 0
      let i;
      for (i in subgroups) { name = subgroups[i]; tot += +d[name] }
      // Now normalize
      for (i in subgroups) { name = subgroups[i]; d[name] = d[name] / tot * 100 }
    })

    //stack the base? --> stack per subgroup
    const stackedData = d3.stack()
      .keys(subgroups)
      (base)

    // Show the bars
    svg.append("g")
      .selectAll("g")
      // Enter in the stack base = loop key per key = group per group
      .data(stackedData)
      .join("g")
      .attr("fill", d => color(d.key))
      .selectAll("rect")
      // enter a second time = loop subgroup per subgroup to add all rectangles
      .data(d => d)
      .join("rect")
      .attr("x", d => x(d.data.group))
      .attr("y", d => y(d[1]))
      .attr("height", d => y(d[0]) - y(d[1]))
      .attr("width", x.bandwidth())
  })


})(jQuery);
