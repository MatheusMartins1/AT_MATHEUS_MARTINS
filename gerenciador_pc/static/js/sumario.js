(function ($) {

  "use strict";
  function insereLi(id, nome) {
    $('<li><a href="#' + id + '">' + nome + '</a></li>').appendTo("#menu_relatorio_sumario>details>ul");
  }


  $(document).ready(function () {

    $('#menu_relatorio_sumario').toggleClass('active');

    insereLi("intro", "Relatório do projeto")
    
    var i, tp, nmTp;
    for (let index = 2; index < 10; index++) {

      i = index
      i = i.toString();
      tp = "tp" + i
      nmTp = "TESTE DE PERFORMANCE " + i

      insereLi(tp, nmTp)

      if (index == 5) {
        insereLi("implantacao_django", "Implantação do Django")
      }
    }

  });


})(jQuery);
