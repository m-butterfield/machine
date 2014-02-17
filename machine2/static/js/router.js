define([
    'backbone'
], function(Backbone) {
    var Router = Backbone.Router.extend({

        routes: {
            "examples/:exampleNumber": 'loadExample',
            "": "defaultRoute"
        },

        initialize: function(options) {
            this.exampleViews = options.exampleViews;
        },

        defaultRoute: function() {
            this.currentView = this.exampleViews[0];
            this.loadExample(1);
        },

        loadExample: function(exampleNumber) {
            var viewIndex = Number(exampleNumber) - 1;
            this.currentView && this.currentView.close();
            this.currentView = this.exampleViews[viewIndex];
            this.currentView.render();
        }
    })
    return Router;
});