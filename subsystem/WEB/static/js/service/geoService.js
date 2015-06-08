app.service('geoService', function ($rootScope, $http) {

    var service = {

        getAddress: function (lng, lat, callback) {

            qq.maps.convertor.translate(new qq.maps.LatLng(lat, lng), 1, function (res) {
                var latLng = new soso.maps.LatLng(res[0].lat, res[0].lng);
                var geocoder = new soso.maps.Geocoder();

                geocoder.setComplete(function (e) {
                    callback(0, e.detail.address)
                })

                geocoder.setError(function () {
                    callback(1, "获取失几")
                    console.log("get address failed")
                })

                geocoder.getAddress(latLng)

            })
        },

        getGeo: function (callback) {

            var ua = navigator.userAgent.toLowerCase();

            if ("micromessenger" === ua.match(/MicroMessenger/i)) {
                wx.ready(function () {
                    wx.getLocation({
                        success: function (res) {
                            var latitude = res.latitude; // 纬度，浮点数，范围为90 ~ -90
                            var longitude = res.longitude; // 经度，浮点数，范围为180 ~ -180。
                            var speed = res.speed; // 速度，以米/每秒计
                            var accuracy = res.accuracy; // 位置精度
                            alert("get location from weixin success")
                            callback(0, longitude, latitude)
                        },
                        error: function () {
                            alert('获得地理信息失败')
                            callback(-1, "", "")
                        }
                    })
                })
            } else {
                var config = {enableHighAccuracy: true, timeout: 5000, maximumAge: 10000};
                navigator.geolocation.getCurrentPosition(function (position) {
                    var lng = position.coords.longitude;
                    var lat = position.coords.latitude;
                    callback(0, lng, lat)
                }, function (error) {
                    alert("获得地理信息失败")
                    callback(-1, "", "")
                }, config)
            }
        }

    }
    return service
})
