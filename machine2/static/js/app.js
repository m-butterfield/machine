define([
    'backbone',
    'views/example_one',
    'views/example_two'
], function(Backbone, ExampleOneView, ExampleTwoView) {

    var exampleOneView = new ExampleOneView({
        el: $("#machine-example1")
    });

    var exampleTwoView = new ExampleTwoView({
        el: $("#machine-example2")
    });

    var ViewController = Backbone.View.extend({

        events: {
            "click #example-1": "showOneView",
            "click #example-2": "showTwoView"
        },

        viewOne: exampleOneView,
        viewTwo: exampleTwoView,

        showOneView: function(event) {
            event.preventDefault();
            this.viewTwo.close();
            this.viewOne.render();
        },

        showTwoView: function() {
            event.preventDefault();
            this.viewOne.close();
            this.viewTwo.render();
        }

    });

    var viewController = new ViewController({
        el: $("#view-controller")
    });

});
