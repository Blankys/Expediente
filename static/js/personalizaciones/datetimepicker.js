$(document).ready(function () {
	$(".fecha").datetimepicker({
		format: "dd/mm/yyyy",
		autoclose: true,
        todayBtn: true,
		todayHighlight: true,
		minView: "day",
		language: "es",
		pickerPosition: "top-right"
	});
	
	$(".hora").datetimepicker({
		format: "HH:ii:ss",
		autoclose: true,
        todayBtn: true,
		todayHighlight: true,
		maxView: "day",
		language: "es",
		pickerPosition: "top-right"
	});
});
