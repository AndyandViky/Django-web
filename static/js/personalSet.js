

$(function(){
	$('.set_title>span').on('click',function(){
		layer.open({
			content: $('#user_info_edit'),
			type:1,
			title:"信息编辑",
			area: ['400px', '440px'], //宽高,
		});
	});
    $('#btn').on('click',function(){
        var $sex = $('#sex').val();
        var $email = $('#email').val();
        if($sex!="男" && $sex!="女" && $sex!="mail" && $sex!="femail")
        {
            layer.alert("性别填写有误！")
            $('#sex').val("");
            return false;
        }
        if(/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/.test($email)==false){
            layer.alert("邮箱填写有误！");
            $('#email').val("");
            return false;
        }
        else{
            layer.alert("修改成功！");
        }
    });
});