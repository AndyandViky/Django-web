window.onload=function(){
    var targetLongitude;
    var targetlatitude;
    var targetAdress = document.getElementById('adress').innerHTML;
    AMap.service('AMap.Geocoder',function(){//回调函数
        //实例化Geocoder
        geocoder = new AMap.Geocoder({
            city: "全国"//城市，默认：“全国”
        });
        //TODO: 使用geocoder 对象完成相关功能
        geocoder.getLocation(targetAdress, function(status, result) {
            if (status === 'complete' && result.info === 'OK' && result.geocodes.length) {
                targetLongitude = result.geocodes[0].location.lng;
                targetlatitude = result.geocodes[0].location.lat;
            }else{
                alert("获取经纬度失败");
            }
        });
    })
    var mapObj = new AMap.Map('mapContainer');
    mapObj.plugin('AMap.Geolocation', function () {
        geolocation = new AMap.Geolocation({
            enableHighAccuracy: true,//是否使用高精度定位，默认:true
            timeout: 10000,          //超过10秒后停止定位，默认：无穷大
            maximumAge: 0,           //定位结果缓存0毫秒，默认：0
            convert: true,           //自动偏移坐标，偏移后的坐标为高德坐标，默认：true
            showButton: true,        //显示定位按钮，默认：true
            buttonPosition: 'LB',    //定位按钮停靠位置，默认：'LB'，左下角
            buttonOffset: new AMap.Pixel(10, 20),//定位按钮与设置的停靠位置的偏移量，默认：Pixel(10, 20)
            showMarker: true,        //定位成功后在定位到的位置显示点标记，默认：true
            showCircle: true,        //定位成功后用圆圈表示定位精度范围，默认：true
            panToLocation: true,     //定位成功后将定位到的位置作为地图中心点，默认：true
            zoomToAccuracy:true      //定位成功后调整地图视野范围使定位位置及精度范围视野内可见，默认：false
        });
        mapObj.addControl(geolocation);
        geolocation.getCityInfo(function(status,result){
                AMap.service(["AMap.Driving"], function() {
                    var transOptions = {
                        map: mapObj,
                        city: status.name,
                        panel:'panel',                            //具体路线说明
                        policy: AMap.DrivingPolicy.LEAST_TIME //最短时间乘车策略
                };
                var driving = new AMap.Driving(transOptions);
            //根据起、终点坐标查询路线
                driving.search([result.center[0], result.center[1]], [targetLongitude, targetlatitude]);
                
                });
        //[{keyword:position.coords,city:position.city},{keyword:'三明',city:'福建'}]
        }); 
        //geolocation.getCurrentPosition(position) //精准定位
        //geolocation.getCityInfo(status,result);  //定位到城市
    });
}