
**Important note:**
Nobody is maintaining this codebase right now. Anyone who needs a fix will need to submit a Pull Request with the required changes.

---

SABconnect++ adds one-click 'Send to SABnzbd' buttons to many popular NZB index sites.

You also get a taskbar button that allows you to keep an eye on your SABnzbd: current downloads, pause (individual downloads, or pause all), or remove individual queued downloads.

## Installation

### Chrome
Install SABconnect++ at our [Chrome Web Store page](https://chrome.google.com/webstore/detail/okphadhbbjadcifjplhifajfacbkkbod).

### Firefox
To install on Firefox (version 109 or later):
1. Download the extension files from this repository
2. Open Firefox and navigate to `about:debugging#/runtime/this-firefox`
3. Click "Load Temporary Add-on"
4. Navigate to the extension directory and select the `manifest.json` file

**Note:** For permanent installation, the extension needs to be packaged and signed by Mozilla or installed as a developer extension.

## Features

  * One-click NZB downloads for the following sites:
    * binsearch.info (binsearch.net)
    * bintube.com
    * dognzb.com
    * fanzub.com
    * nzbclub.com
    * nzbindex.com (nzbindex.nl)
    * omgwtfnzbs.me
    * yubse.com
    * animezb.com
    * animenzb.com
    * Any Newznab-based indexer
  * Context menu option for sending links to SABnzbd
  * Options page that looks consistent with Chrome's own options layout
  * Download speed graph
  * Pause individual downloads
  * Pause all downloads
  * Remove individual downloads
  * Desktop notifications (Download Complete/Failed)
  * Storage sync for settings

SABconnect++ is a fork of the now unmaintained Chrome extension [SABconnect](http://code.google.com/p/sabconnect/).
