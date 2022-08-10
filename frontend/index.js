var HelloWorld = /** @class */ (function () {
    function HelloWorld() {
    }
    HelloWorld.prototype.test = function () {
        console.log("test");
    };
    HelloWorld.prototype.test2 = function () {
        return "hello";
    };
    HelloWorld.main = function (args) {
        console.log("Hello World");
    };
    return HelloWorld;
}());
HelloWorld.main([]);
