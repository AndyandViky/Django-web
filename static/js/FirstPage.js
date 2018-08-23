

$(function(){
	autoBanner();
	searchEvent();
})

//自动banner
function autoBanner(){
	$("#banner>img").eq(0).show().siblings().hide();
	$(".tab").eq(0).addClass("bg");
	var i=0;
	var timer=setInterval(function(){
		Show(i);
		i=(i+1)%8;
	},3000);
	$(".tab").hover(function(){
		clearInterval(timer);
		var index=$(this).index();
		Show(index);
	},function(){
		var index=$(this).index();
		timer=setInterval(function(){
		Show(index);
		index=(index+1)%8;
	},3000);
	});

}
function Show(i){
	$("#banner>img").eq(i).fadeIn().siblings().fadeOut();
	$(".tab").eq(i).addClass("bg").siblings().removeClass("bg");
}