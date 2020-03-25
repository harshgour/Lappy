<script>
var slider = document.getElementById("myRange");
var output = document.getElementById("price");
output.innerHTML = slider.value;
slider.oninput = function() {
  output.innerHTML = this.value;
}
</script>
