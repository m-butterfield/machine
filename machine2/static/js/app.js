define([
    'views/example_one'
], function(ExampleOneView) {

    var exampleOneView = new ExampleOneView({
        el: $("#machine-example1")
    });

    exampleOneView.render();

});
