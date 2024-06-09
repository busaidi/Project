// static/js/admin_map.js
(function($) {
    $(document).ready(function() {
        if (typeof ol !== 'undefined') {
            var map = window.map || window.geometry_0_map;
            if (map) {
                map.setCenter(
                    ol.proj.fromLonLat([57.0, 21.0]), // Coordinates of Oman
                    7 // Zoom level
                );
            }
        }
    });
})(django.jQuery);
