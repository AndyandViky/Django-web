//创建景点元素
function createScenic(data){
	var ul = $('.scenicSport');
	for(var i=0;i<data.length;i++){
		ul.append('<li><div class="imgBox"><a href="'+data[i].id+'"><img src='+"/"+data[i].image+' alt=""></a></div><div class="img-decritionBox"><h4>'+data[i].name+'</h4><p class="decrition">'+data[i].detail+'<a href='+data[i].href+'>[详情]</a></p></div></li>')
	}
}