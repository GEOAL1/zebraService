app.controller("bikeInfoController", function ($timeout, $scope, $http, userService, wxService, bikeService, geoService) {
    $scope.getBikeInfo = function (bike_id) {
        bikeService.getBikeInfo(bike_id,function(state,data){
            if(state == 0) {
                $scope.bike = data.body;
                if($scope.bike.lock_state==0) {
                    $scope.bike.nextLockState = "锁车"
                    $scope.bike.curLockState="未锁"
                }else{
                    $scope.bike.nextLockState = "解锁"
                    $scope.bike.curLockState="已锁"
                }
            }
        })
        updateClock();
    }

    $scope.bikeLight = bikeService.bikeLight
    $scope.bikeVoice = bikeService.bikeVoice


    $scope.lockBike = function (bike) {
        bikeService.lockBike(bike)
    }

    $scope.callUs = function (bike) {
        alert("callUs")
    }

    $scope.navigate = function (bike) {
        bikeService.bikeNavigate(bike)
    }

    $scope.finishOrderBike = function () {
        bikeService.finishOrder($scope.orderID, function (state, data) {

        })
    }

    $scope.orderID = GetQueryString("order_id")


    var updateClock = function () {
        $scope.clock = new Date();
        $timeout(function () {
            $scope.refreshInfo()
        }, 30000);
    };


    $scope.refreshInfo = function () {
        bikeService.getOrderByOrderID($scope.orderID, function (state, data) {
            if (state == 0) {
                $scope.order = data.body
                $scope.getBikeInfo($scope.order.bike_id)
            } else {
                $scope.refreshInfo()
            }
        })
    }


    if($scope.orderID == null) {
        userService.getUserOrder(function (statue, data) {
            if (statue == 0) {
                $scope.orderID = data.body.order_id
                $scope.refreshInfo()
                updateClock()
            }
            else {
                alert("你还没订车,快去选车吧")
                window.location.href = "/static/panel.html"
            }
        })
    }else{
        $scope.refreshInfo()
        updateClock()
    }
})