app.service('userService', function ($rootScope, $http) {
    var sendCmd = function (url, method, data, callback) {
        var http_config = {};
        if (method == "GET") {
            http_config = {
                method: "GET",
                url: url,
                params: data,
                timeout: 5000,
            }
        } else {
            http_config = {
                method: "POST",
                url: url,
                data: $.param(data),
                timeout: 5000,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            }
        }

        $http(http_config).success(function (data, status, headers, config) {
            if (data.errorCode != 0) {
                console.log(data.errorCode + " : " + data.errorMeg)
            }
            callback(data.errorCode, data)
        }).error(function (data, status, headers, config) {

            if (status == 403) {
                alert("登录超时，请重新登录")
                window.location.href = "/static/login.html"
            }
            alert(status)

            callback(-1, {errorCode: -1, errorMeg: status})
        });
    };

    var service = {
        getUserInfo: function (cb) {
            sendCmd("/wx/u/info", "GET", {}, function (state, data) {
                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },

        login: function (phone, password, cb) {
            data = {"un": phone, "pw": password}
            sendCmd("/wx/u/login", "POST", data, function (statue, data) {
                if (statue == 0) {
                    window.location.href = "/";
                } else {
                    alert(data.errorMeg);
                }

                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },

        register: function (regObject, cb) {
            sendCmd("/wx/u/reg", "POST", regObject, function (statue, data) {
                if (statue == 0) {
                    alert("注册成功");
                    window.location.href = "/";
                } else {
                    alert("注册失败：" + data.errMsg);
                }

                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },
        getUserOrder: function (callback) {
            sendCmd('/wx/u/order', "GET", {}, function (state, data) {
                callback(state, data)
            })
        },

        recharge: function(rechargeNum,cb) {
            sendCmd("/wx/a/recharge", "POST", {rechargeNum: rechargeNum}, function (statue, data) {
                if (statue == 0) {
                    alert("充值成功，跳转到主页")
                    window.location.href = "/";
                } else {
                    alert("充值失败：" + data.errMsg);
                }
                if (cb != undefined) {
                    cb(state, data)
                }
            })
        }
    }
    return service
})
