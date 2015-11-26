$(function(){
	$('#add_more_measurement').click(function() {
        var form_idx = $('#id_form-TOTAL_FORMS').val();
        $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
        $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
		$('.MeasurementFormSet div input').change(measurement_change);
		$('.MeasurementFormSet select').change(calculate_total_measurement);
    });
	
	$('.MeasurementFormSet div input').change(measurement_change);
	$('.MeasurementFormSet select').change(calculate_total_measurement);
	$('.invoice_table tbody tr').each(function(){ 
		
		link = $(this).find('.amount a').attr('href');
		if(link) {
			$(this).find('td:not(".amount")').each(function(){
				html = $(this).html(); 
				at = "<a href='"+link+"'>"+html+"</a>"; 
				$(this).html(at); 
			});
		}
	});

    $('.paymentForm select[name="payment_towards"]').change(function(){
        $('.paymentForm input[name="remaining_amount"]').closest('tr').toggle();
        $('.paymentForm .SumoSelect').toggle();
    });

	$('.menu ul li').click(function(){
		$('.menu ul li').removeClass("selected");
		$(this).addClass("selected");
	});
	
	$(".header").click(function () {
		//getting the next element
		$content = $(this).next();
		//checking if its already visible
		if (!($content.is(":visible"))) {
			//no - its hidden - slide all the other open tabs to hide
			$(".content").slideUp("fast");
			//open up the content needed
			$content.slideToggle(500);
		}
	});
	
	
	
	$(".paymentForm input[name='amount']").change(function () {
		//getting the next element
		amt = $(".paymentForm input[name='amount']").val();
		rem_elem = $(".paymentForm input[name='remaining_amount']");
		rem_elem.val(amt);
		$(".SumoSelect li").removeClass('selected')
		rem_changed();
	});
	
	$(".SumoSelect li").click(function(){
		id = $(this).attr('data-val');
		balance = $(".SumoSelect select option#"+id).attr('data-balance');
		rem = parseInt($(".paymentForm input[name='remaining_amount']").val());
		if($(this).hasClass('selected')) {
			rem -= balance;
		}
		else {
			rem += parseInt(balance);
		}
		if(rem<0) {
			$("p.warning").removeClass('nodisplay');
		}
		else {
			$("p.warning").addClass('nodisplay');
		}
		$(".paymentForm input[name='remaining_amount']").val(rem);
		rem_changed();
	});
	
	
});

function rem_changed() {
	amt = $(".paymentForm input[name='remaining_amount']").val();
	if(amt<=0) {
		$(".SumoSelect li").not(".selected").addClass('disabled');
	}
	else {
		$(" .SumoSelect li").removeClass('disabled');
		//$(".paymentForm .selector h2 * ").css({'background-color': 'initial'})
	}
}

function validPayment() {
	rem =$(".paymentForm input[name='remaining_amount']").val();
    towards = $(".paymentForm select[name='payment_towards']").val();
    //alert(towards)
	if(amt > 0 && towards == "1" ) {
		alert("Please Apply the remaining amount "+rem+" to any other invoices.")
		return false;
	}
}
function measurement_change() {
		filled = 0;
		hwl =1
		$(this).parent().find('input[type!="submit"]').each(function(){
			if($(this).val() && !isNaN($(this).val())) {
				hwl *= parseInt($(this).val())
				filled =1;
			}
		});
		if(filled == 0) {
			$($(this).parent()).find('.hwl span').text(0);
			$(this).parent().find('.hwl').hide();
		}
		else {
			$($(this).parent()).find('.hwl span').text(hwl);
			$(this).parent().find('.hwl').show();
		}
		calculate_total_measurement();
}
function calculate_total_measurement() {
	sum = 0;
	$('.each_total').each(function(){
		val = Number($(this).html());
		unit = $(this).closest('div').find('select').val();
		if(unit == 1) {
			val = val * 12;
		}
		sum+=val;
	})
	feets = sum / 12;
	if($('select#cunit').val()==1) {
		$('#total_measurement').html(feets+" feets");
		unitcost = Number($('input#unitcost').val());
		if(unitcost > 0) {
			cost = feets * unitcost
			$('#total_cost').html(cost)
			$('#total_cost').parent().show();
		}
		else {
			$('#total_cost').parent().hide();
		}
	}
	else {
		$('#total_measurement').html(sum+" inches");
		unitcost = Number($('input#unitcost').val());
		if(unitcost > 0) {
			cost = sum * unitcost
			$('#total_cost').html(cost)
			$('#total_cost').parent().show();
		}
		else {
			$('#total_cost').parent().hide();
		}
	}
	if(sum<=0) {
		$('#total_measurement').parent().hide();
		$('.rateperunit').hide();
	}
	else {
		$('#total_measurement').parent().show();
		$('.rateperunit').show();
	}
}