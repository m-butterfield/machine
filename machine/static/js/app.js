define([
    'backbone',
    'router',
    'views/main_links',
    'views/example_one',
    'views/example_two',
    'views/example_three',
], function(Backbone, Router, MainLinksView,
            ExampleOneView, ExampleTwoView, ExampleThreeView) {

    var exampleOneView = new ExampleOneView({
        el: $("#machine-example1")
    });

    var exampleTwoView = new ExampleTwoView({
        el: $("#machine-example2")
    });

    var exampleThreeView = new ExampleThreeView({
        el: $("#machine-example3")
    });

    var router = new Router({
        exampleViews: [
            exampleOneView,
            exampleTwoView,
            exampleThreeView
        ]
    });

    var mainLinksView = new MainLinksView({
        el: $("#main-links"),
        router: router
    });

    Backbone.history.start({pushState: true});

});
