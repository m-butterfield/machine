define([
    'backbone',
    'views/view_controller',
    'views/example_one',
    'views/example_two',
    'views/example_three'
], function(Backbone, ViewController, ExampleOneView, ExampleTwoView, ExampleThreeView) {

    var exampleOneView = new ExampleOneView({
        el: $("#machine-example1")
    });

    var exampleTwoView = new ExampleTwoView({
        el: $("#machine-example2")
    });

    var exampleThreeView = new ExampleThreeView({
        el: $("#machine-example3")
    })

    var viewController = new ViewController({
        el: $("#view-controller"),
        exampleViews: [exampleOneView, exampleTwoView, exampleThreeView]
    });

});
