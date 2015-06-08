app.controller("panelController", function ($scope, userService, wxService, bikeService, geoService) {
    $scope.search = {
        distance: 5000,
        bike_id: ""
    }

    $scope.searchBike = function () {
        $scope.getNearBike()
        $('#search-menu').slideToggle()
    }
    $scope.touchon = function () {
        $(document).on('touchmove', function (e) {
            e.preventDefault();
        });
    }

    $scope.QRScanOrder = function () {
        wx.scanQRCode({
            needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
            scanType: ["qrCode", "barCode"], // 可以指定扫二维码还是一维码，默认二者都有
            success: function (res) {
                var bikeid = res.resultStr; // 当needResult 为 1 时，扫码返回的结果
                $scope.bikeOrder(bikeid)
            }
        });
    }

    $scope.touchoff = function () {
        $(document).off('touchmove');
    }

    $scope.openBikeLV = function (bike) {
        bikeService.bikeLight(bike)
        bikeService.bikeVoice(bike)
    }

    $scope.bikeNavigate = bikeService.bikeNavigate
    $scope.bikeOrder = bikeService.bikeOrder

    $scope.openOrderModal = function (bike) {
        $('#myModal').modal('show')
        $scope.selectBike = bike;
        $event.preventDefault()
    }


    userService.getUserInfo(function (status, data) {
        if (status === 0) {
            $scope.user = data.body;
        } else {
            alert("获得用户信息失败，正在重新加载")
            window.location.href = "/"
        }
    })

    $scope.getNearBike = function () {
        $scope.touchon()
        $scope.user_load_ok = false

        bikeService.getNearBike($scope.lng, $scope.lat, $scope.search, function (status, data) {
            if (status == 0) {
                $scope.nearCars = data.body
                $scope.nearCars.forEach(function (bike) {
                    geoService.getAddress(bike.longitude, bike.latitude, function (t, address) {
                        bike.address = address
                        console.log(address)
                        $scope.$digest()
                    })
                })

            }
            else {
                alert("获得附近的车失败")
            }
            $scope.touchoff()
            $scope.user_load_ok = true


        })
    }

    geoService.getGeo(function (status, lng, lat) {
        if (status == 0) {
            $scope.lng = lng;
            $scope.lat = lat;
        } else {
            $scope.lng = 116.397128
            $scope.lat = 39.916527
        }

        $scope.getNearBike()


    });


})

