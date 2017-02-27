/* jshint globalstrict: true, undef: true, unused: true, esversion: 6 */
/* global $ */
'use strict';

$(() => {
    // Open all non-local links in new tab
    // This allows us to use markdown syntax without worrying about target="_blank"
    $('a[href^=http]').attr('target', '_blank');
});
