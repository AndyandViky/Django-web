

$(function(){
    djugePassword();
})


//判断文本框是否输入正确的格式
function djugePassword(){
    $('.login input[type="submit"]').on('click',function(){
        var $email = $('#email').val();
		var info="";
        var $password1 = $('.password').eq(0).val();
		var $password2 = $('.password').eq(1).val();
        if($password1!=$password2){
            info = "输入密码不一致！请重新输入"
            animate(info);
			$('.password').eq(0).val("");
			$('.password').eq(1).val("");
            return false;
		}
        if($email!=null){
            if(/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/.test($email)==false){
                info = "用户名格式不正确！请重新输入"
                animate(info);
                $('#email').val("");
                return false;
            }
        }
    })
}
function animate(info){
    $('.tip-info').text(info);
    $('.tip-info').animate({
        opacity:1,
    },300,function(){
		$('.tip-info').animate({
        	opacity:0,
    	},2000) 
	}) 
}