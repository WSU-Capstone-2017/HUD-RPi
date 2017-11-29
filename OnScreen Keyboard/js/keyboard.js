$(function(){
	var $write = $('#write'),
		shift = false,
		capslock = false;
		
	$('#keyboard li').click(function(){
		var $this = $(this),
			character = $this.html();//continues lowercase
			
			//left and right shift buttons
			if ($this.hasClass('left-shift') || $this.hasClass('right-shift')){
				$('.letter').toggleClass('uppercase');
				$('.symbol span').toggle();
				shift = (shift === true) ? false : true;
				capslock = false;
				return false;
			}
			
			//caps lock
			if ($this.hasClass('capslock')) {
            $('.letter').toggleClass('uppercase');
            capslock = true;
            return false;
			}
         
        // Delete
        if ($this.hasClass('delete')) {
            var html = $write.html();
             
            $write.html(html.substr(0, html.length - 1));
            return false;
			}
         
        // Characters
        if ($this.hasClass('symbol')) character = $('span:visible', $this).html();
        if ($this.hasClass('space')) character = ' ';
        if ($this.hasClass('tab')) character = "\t";
        if ($this.hasClass('enter')) character = "\n";
         
        // Uppercase letter
        if ($this.hasClass('uppercase')) character = character.toUpperCase();
         
        // normal keys after shift button is used
        if (shift === true) {
            $('.symbol span').toggle();
            if (capslock === false) $('.letter').toggleClass('uppercase');
             
            shift = false;
        }
         
        // writes character to screen
        $write.html($write.html() + character);
    });
});