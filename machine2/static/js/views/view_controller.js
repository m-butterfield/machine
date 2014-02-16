define([
    'backbone'
], function(Backbone) {
    var ViewController = Backbone.View.extend({

        events: {
            "click .example-link": "showExample"
        },

        initialize: function(options) {
            this.exampleViews = options.exampleViews;
            this.currentView = this.exampleViews[0];
            this.currentView.render();
        },

        showExample: function(event) {
            event.preventDefault();
            this.currentView.close();
            var viewIndex = Number(event.target.id.split('-')[1]) - 1;
            this.currentView = this.exampleViews[viewIndex];
            this.currentView.render();
        }

    });
    return ViewController;
});