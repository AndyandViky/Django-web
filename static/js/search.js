$(function(){
    searchEvent();
})
function searchEvent(){
	//搜索点击事件
	$('#bt').on('click',function(){
		var value=$('#txt').val();
		search(value);
	});
	//键盘输入事件
	$('#txt').on('keydown',function(e){
		if(e.keyCode==13)
		{
			var value=$('#txt').val();
			search(value);
			return false;
		}
	});

}
function search(value){
	if(value.indexOf('首页')!=-1)
	{
		location.href='/';
	}
	else if(value.indexOf('景色')!=-1 || value.indexOf('美景')!=-1 || value.indexOf('乡村')!=-1)
	{
		location.href='/country/Scinces/';
	}
	else if(value.indexOf('游')!=-1)
	{
		location.href='/country/Tourists/';
	}
	else if(value.indexOf('文化')!=-1)
	{
		location.href='/country/Culturals/';
	}
	else if(value.indexOf('美食')!=-1)
	{
		location.href='/country/Foods/';
	}
	else if(value.indexOf('最美')!=-1)
	{
		location.href='/country/btCountry/';
	}
	else{
		location.href='/country/404/';
	}
}