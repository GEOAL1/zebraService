app.controller("mapController", function ($scope) {
    //得到我的位置
    var myLocation = {
        lng: 116.461366,
        lat: 39.964285
    }

    var carsList = [
        {
            id: 123,
            name: "小马快跑1",
            price: "10",
            address: "东直门外大街",
            distance: "500",
            power: 50,
            drivingRanger: 100,
            lng: 116.461366,
            lat: 39.964235,
            carImg: "img/car.jpg"
        },
        {
            id: 456,
            name: "小马快跑2",
            price: "10",
            address: "东直门外大街",
            distance: "500",
            power: 50,
            drivingRanger: 100,
            lng: 116.461366,
            lat: 39.96511,
            carImg: "img/flag.png"
        }
    ];

    var template = '<div id="tip">' +
        '<img src="{1}" width="30" height="45" class="fl"/>' +
        '<div id="{0}" style="overflow: hidden;">' +
        '<div class="line1"><span>{2}</span><span>{3}</span><span>电量{4}%</span></div>' +
        '<div><span>{5}/公里</span><span>6</span><span>续航：{7}公里</span></div>' +
        '</div>' +
        '<div class="btn"><input type="button" onclick="alert(\'find car {0}\')" value="寻车"/><input type="button" onclick="mapUtile.getWalkRoute(\'{8}\',\'{9}\')" value="导航"/><input type="button"  value="详情"/><input type="button" value="另外"/></div>' +
        '</div>';

    //绑定数据
    $scope.carsList = carsList;
    $scope.mylocation = myLocation;
    mapUtile.init('map_canvas', "img/car.jpg");
    mapUtile.setFouces(myLocation.lng, myLocation.lat)

    carsList.forEach(function (car) {
        car.distance = mapUtile.getDistance(myLocation, car);
        mapUtile.getAddress(car.lng, car.lat, function (address) {
            car.address = address;
            var sContent = stringFormat(template, car.id, "img/car.jpg", car.name, car.address, car.power, car.price, car.distance, car.drivingRanger, car.lng, car.lat);
            mapUtile.drawNearCar(car, sContent)
        });

    })


})