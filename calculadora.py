<!-- Código "emprestado" do site http://pt.wikipedia.org/wiki/XHTML -->

<form name="calcform" method="post" action="">
   <fieldset>
      <legend>Devin - Calculadora Simples</legend>

      <label for="valor1">Digite o valor <strong>1</strong>:</label>
      <input type="text" name="valor1" id="valor1" />

      <label for="valor2">Digite o valor <strong>2</strong>:</label>
      <input type="text" name="valor2" id="valor2" />

      <label for="oper">Selecione a operação:</label>
      <select name="oper" id="oper">
         <option value="somar">Somar</option>
         <option value="subtrair">Subtrair</option>
         <option value="multiplicar">Multiplifcar</option>
         <option value="dividir">Dividir</option>
      </select>

      <label for="res">Resultado:</label>
      <input type="text" name="res" id="res" />

      <input type="button" value="Calcular" class="botao" onClick="calcular(document.calcform.oper.value)"/>
   </fieldset>
</form>