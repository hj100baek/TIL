```js
// targetFunction을 실행한 후 hookFunction을 실행
export function createHook(obj, targetFunction, hookFunction) {
    let temp = obj[targetFunction]
    obj[targetFunction] = function (...args) {
        let ret = temp.apply(this, args)
        if (ret && typeof ret.then === 'function') {
            return ret.then((value)=>{hookFunction([value, args]); return value;})
        } else {
            hookFunction([ret, args])
            return ret
        }
    }
}
```
