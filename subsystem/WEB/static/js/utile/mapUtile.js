//操作对象
mapUtile = function () {
    //utile 函数
    var userCurAddress;

    function getLocation(callback) {
        var options = {
            enableHighAccuracy: true,
            maximumAge: 4000,
            timeout: 5000
        }

        //成功时
        function onSuccess(position) {
            //经度
            userPosition.lng = position.coords.longitude;
            //纬度
            userPosition.lat = position.coords.latitude;

            callback(userPosition);
        }


        //失败时
        function onError(error) {
            alert(error.code);

            switch (error.code) {
                case 1:
                    alert("位置服务被拒绝");
                    break;

                case 2:
                    alert("暂时获取不到位置信息");
                    break;

                case 3:
                    alert("获取信息超时");
                    callback(userPosition);

                    break;

                case 4:
                    alert("未知错误");
                    break;
            }

        }

        if (navigator.geolocation) {
            //浏览器支持geolocation
            navigator.geolocation.getCurrentPosition(onSuccess, onError, options);

        } else {
            alert("浏览器不支持获取位置")
        }

    }

    var map;
    var centerPosition = {lat: 0, lng: 0};
    var GeoUtile;

    //内部函数
    var centerMarker;
    var userPosition;

    var handleInit = function (mapDivId, carImageSrc) {
        //初始化地图及工具
        map = new BMap.Map(mapDivId);
        myGeo = new BMap.Geocoder();
        carIcon = new BMap.Icon(carImageSrc,
            new BMap.Size(30, 30), {
                anchor: new BMap.Size(7, 25)
            });

        /*
         map.centerAndZoom(new BMap.Point(116.404, 39.915), 13)
         */
        map.addControl(new BMap.NavigationControl());
        map.addControl(new BMap.ScaleControl());
        map.setCurrentCity("北京");
        map.addControl(new BMap.OverviewMapControl());
        map.addControl(new BMap.MapTypeControl());
    }

    var handleFouces = function (x, y) {
        gpsPoint = new BMap.Point(x, y)
        BMap.Convertor.translate(gpsPoint, 2, function (point) {
            centerMarker = new BMap.Marker(point);        // 创建标注
            map.addOverlay(centerMarker);
            centerPosition.lng = x;
            centerPosition.lat = y;
            map.centerAndZoom(point, 17);
            myGeo.getLocation(new BMap.Point(centerPosition.lng, centerPosition.lat), function (result) {
                userCurAddress = result.address;
            })
        });
    }

    //外部函数
    var handleNearCar = function (car, winCarTemplate) {
        var myIcon = new BMap.Icon(car.carImg,
            new BMap.Size(30, 30), {
                anchor: new BMap.Size(7, 25)
            });

        var mark = new BMap.Marker(new BMap.Point(car.lng, car.lat), {icon: myIcon});        // 创建标注
        map.addOverlay(mark);

        mark.addEventListener("click", function (e) {
            var opts = {
                width: 100,     // 信息窗口宽度
                height: 50,     // 信息窗口高度
                title: "车辆信息"    // 信息窗口标题
            }

            var infoWindow = new BMap.InfoWindow(winCarTemplate);  // 创建信息窗口对象
            map.openInfoWindow(infoWindow, this.getPosition());
        });
    };


    return {
        //完成初始化地图
        init: function (mapDivId, carImageSrc) {
            handleInit(mapDivId, carImageSrc);
        },

        //设置地图当前焦点
        setFouces: function (x, y) {
            handleFouces(x, y);
        },

        //画附件的车
        drawNearCar: function (car, template) {
            handleNearCar(car, template)
        }
        ,
        //得到两点间的距离
        getDistance: function (x, y) {
            var pointA = new BMap.Point(x.lng, x.lat);
            var pointB = new BMap.Point(y.lng, y.lat);
            return map.getDistance(pointA, pointB).toFixed(0);
        },

        getUserPoisition: function (callback) {
            getLocation(callback);
        },

        getAddress: function (x, y, callback) {
            myGeo.getLocation(new BMap.Point(x, y), function (result) {
                callback(result.address);
            })
        },

        getWalkRoute: function (x, y) {
            var walking = new BMap.WalkingRoute(map, {renderOptions: {map: map, autoViewport: true}});
            /*alert(centerMarker.getPosition());
             alert(target);*/
            var pointB = new BMap.Point(x, y);
            alert(x + " " + y)
            walking.search(centerMarker.getPosition(), pointB);
            /*
             walking.search(centerMarker.getPosition(),"东直门外大街");
             */
        }

    }
}();