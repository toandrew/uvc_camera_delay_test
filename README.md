# uvc_camera_delay_test

## Timer
https://www.jq22.com/webqd2064

```
function TimeLoop() {
    var n = new Date().getTime();
    document.getElementById('timer').innerHTML = '' + n;
}
(function() {
    window['ttt'] = setInterval(function() {
        TimeLoop();
    }, 1);
})();
```

## Capture
```
#python uvc_camera_delay_test.py
```


## Check delay
```
All pics saved in './pics/'
```

