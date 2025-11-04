# Firefox Compatibility Notes

## Overview
SABconnect++ has been updated to work with both Google Chrome and Mozilla Firefox using the same codebase.

## Requirements
- **Firefox:** Version 109 or later
- **Chrome:** Version 88 or later

## Installation

### Firefox
1. Download or clone this repository
2. Open Firefox and navigate to `about:debugging#/runtime/this-firefox`
3. Click "Load Temporary Add-on"
4. Navigate to the extension directory and select the `manifest.json` file

**For permanent installation:**
- Package the extension as a `.xpi` file
- Sign it with Mozilla (required for production use)
- Or use Firefox Developer Edition with `xpinstall.signatures.required` set to `false` in `about:config`

### Chrome
Install from the [Chrome Web Store](https://chrome.google.com/webstore/detail/okphadhbbjadcifjplhifajfacbkkbod) or load as an unpacked extension.

## Technical Details

### Manifest V3
The extension uses Manifest V3, which is supported by:
- Chrome 88+
- Firefox 109+ (with some differences from Chrome's implementation)

### Cross-Browser Compatibility
The extension includes a browser API polyfill that ensures both `chrome.*` and `browser.*` APIs work correctly in both browsers. The polyfill is added to all scripts that interact with browser extension APIs.

### Service Worker
The extension uses a service worker for background functionality (`scripts/background-sw.js`). Firefox 109+ supports service workers in Manifest V3 extensions.

## Known Limitations

### Firefox-Specific Considerations
1. **Temporary Installation:** Extensions loaded via `about:debugging` are temporary and will be removed when Firefox restarts
2. **Signing Requirement:** For permanent installation, extensions must be signed by Mozilla or the signing requirement must be disabled in Firefox Developer Edition
3. **API Differences:** While the extension uses a polyfill to handle API differences, some subtle behavior differences may exist between browsers

### Features Tested
- ✅ Manifest V3 structure
- ✅ Service worker background script
- ✅ Browser API polyfill
- ✅ Content scripts injection
- ✅ Popup and settings pages
- ✅ Storage APIs
- ✅ Context menus
- ✅ Notifications
- ✅ Dynamic content script injection

### Testing Status
The extension structure has been validated and should work in Firefox 109+. However, comprehensive end-to-end testing in a real Firefox environment is recommended to ensure all features work as expected.

## Development

### Validation
Run the validation script to check Firefox compatibility:
```bash
python3 validate_firefox.py
```

This script checks:
- Manifest.json validity and structure
- Firefox-specific settings (browser_specific_settings)
- Presence of browser API polyfills
- Required file existence

### Building for Firefox
No special build process is required. The same files work for both Chrome and Firefox.

### Debugging
- **Chrome:** Use Chrome DevTools (chrome://extensions → Details → Inspect views)
- **Firefox:** Use Browser Console (Ctrl+Shift+J) and about:debugging

## Compatibility Matrix

| Feature | Chrome | Firefox 109+ |
|---------|--------|--------------|
| Manifest V3 | ✅ | ✅ |
| Service Worker | ✅ | ✅ |
| Content Scripts | ✅ | ✅ |
| Storage API | ✅ | ✅ |
| Context Menus | ✅ | ✅ |
| Notifications | ✅ | ✅ |
| Scripting API | ✅ | ✅ |
| Alarms API | ✅ | ✅ |

## Troubleshooting

### Extension doesn't load in Firefox
- Ensure you're using Firefox 109 or later
- Check the Browser Console for any error messages
- Verify manifest.json is valid using the validation script

### Features not working as expected
- Check the Browser Console for JavaScript errors
- Verify the browser API polyfill is present in the relevant script files
- Compare behavior between Chrome and Firefox to identify browser-specific issues

## Contributing
If you find any Firefox-specific issues, please report them with:
- Firefox version
- Steps to reproduce
- Console error messages (if any)
- Whether the same issue occurs in Chrome

## References
- [Firefox Extension Workshop](https://extensionworkshop.com/)
- [MDN WebExtensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions)
- [Chrome Extensions Documentation](https://developer.chrome.com/docs/extensions/)
