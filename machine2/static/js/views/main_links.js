define([
    'backbone'
], function(Backbone) {
    var MainLinksView = Backbone.View.extend({

        events: {
            'click .example-link': 'doNavigate'
        },

        initialize: function(options) {
            this.router = options.router;
        },

        doNavigate: function(event) {
            event.preventDefault();
            this.router.navigate($(event.target).attr('href'), {trigger: true});
        }

    })
    return MainLinksView;
});
