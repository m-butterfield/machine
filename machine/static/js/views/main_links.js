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
            if (window.location.href === event.target.href) {
                Backbone.history.loadUrl(Backbone.history.fragment);
            } else {
                this.router.navigate($(event.target).attr('href'), {
                    trigger: true
                });
            }
        }

    })
    return MainLinksView;
});
