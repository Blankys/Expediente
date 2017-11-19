$(document).ready(function () {
	$(".table-responsive").on("click", ".EliminarRegistro", function (event) {
		event.preventDefault();
		$elemento = $(this);
		alertify.confirm(
			"No se puede recuperar después de eliminar. ¿Estás seguro de continuar?",
			function () {
				$.ajax({
					url: $elemento.data("url"),
					type: "GET",
					dataType: "json",
					success: function (response) {
						if (response.error) {
							alertify.error(response.mensaje);
						}
						else {
							alertify.success(response.mensaje);
							setTimeout(function () { location.reload(true); }, 1000);
						}
					},
					error: function (exception) {
						if (exception.status != undefined) {
							alertify.error(exception.status + " (" + exception.statusText + ")");
						}
					}
				});
			},
			null
		);
	});
});
