({
    baseUrl: ".",
    name: 'main',
    paths: {
        "backbone": '../vendor/backbone',
        "bootstrap": '../vendor/bootstrap',
        "domReady": '../vendor/domReady',
        "jquery": '../vendor/jquery',
        "text": '../vendor/text',
        "underscore": '../vendor/underscore'
    },
    "shim": {
        "backbone": {
            deps: ["jquery", "underscore"],
            exports: "Backbone"
        },
        "bootstrap": ["jquery"]
    },
    out: 'main-build.js',
    findNestedDependencies: true
})
