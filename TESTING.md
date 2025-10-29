# Testing Guide for Firefox Compatibility

## Quick Test Checklist

### Prerequisites
- Firefox 109 or later installed
- Git repository cloned locally

### Basic Loading Test
1. Open Firefox
2. Navigate to `about:debugging#/runtime/this-firefox`
3. Click "Load Temporary Add-on"
4. Browse to the repository directory
5. Select `manifest.json`
6. Verify the extension loads without errors

**Expected Result:** Extension appears in the list with name "SABconnect++" and version "2.0.0"

### Console Check
1. After loading the extension, check the Browser Console (Ctrl+Shift+J)
2. Look for any error messages related to SABconnect++
3. Verify no "Uncaught" errors appear

**Expected Result:** No critical errors in console

### Extension Popup Test
1. Click the SABconnect++ icon in the Firefox toolbar
2. Verify the popup opens without errors
3. Check that all UI elements render correctly

**Expected Result:** Popup displays with SABnzbd connection settings

### Settings Page Test
1. Right-click the extension icon
2. Select "Manage Extension"
3. Click on "Options" or go to Settings
4. Verify the settings page loads

**Expected Result:** Settings page displays correctly with all configuration options

### Content Script Test
1. Navigate to one of the supported sites (e.g., binsearch.info)
2. Open the Browser Console
3. Look for any SABconnect++ related messages or errors

**Expected Result:** Content scripts inject without errors, buttons appear on the page

### Background Service Worker Test
1. Go to `about:debugging#/runtime/this-firefox`
2. Find SABconnect++ in the list
3. Click "Inspect" next to the service worker
4. Check the console for any errors

**Expected Result:** Service worker running without errors

### Storage API Test
1. Open the extension settings
2. Configure a test SABnzbd URL (can be dummy: http://localhost:8080)
3. Save the settings
4. Close and reopen Firefox
5. Load the extension again
6. Check if settings persisted

**Expected Result:** Settings are saved and restored after browser restart

### Browser API Polyfill Test
Check that the polyfill is working:
1. Open Browser Console for the extension
2. Type: `typeof chrome`
3. Type: `typeof browser`
4. Both should return "object"

**Expected Result:** Both `chrome` and `browser` APIs are available

## Advanced Testing

### Context Menu Test
1. Enable context menu in settings
2. Right-click on any link
3. Look for "Send to SABnzbd" option

**Expected Result:** Context menu item appears

### Notification Test
1. Enable notifications in settings
2. If you have SABnzbd running, add a download
3. Wait for completion

**Expected Result:** Desktop notification appears (if enabled)

### Cross-Browser Comparison
If possible, test the same features in Chrome to ensure parity:
1. Load extension in both browsers
2. Test the same workflows
3. Compare functionality

**Expected Result:** Behavior is consistent across browsers

## Validation Script Test
Run the validation script:
```bash
python3 validate_firefox.py
```

**Expected Result:** All checks pass with ✅

## Common Issues and Solutions

### Extension Won't Load
- Check Firefox version (must be 109+)
- Verify manifest.json is valid JSON
- Check Browser Console for specific errors

### Service Worker Errors
- Firefox 109+ is required for service worker support
- Check if service worker is registered in about:debugging

### Content Scripts Not Injecting
- Verify you're on a supported site
- Check permissions in manifest.json
- Look for errors in Browser Console

### Settings Not Persisting
- Check storage permissions
- Verify browser.storage or chrome.storage API is available
- Check Browser Console for storage errors

## Reporting Issues
If you find issues during testing, please report:
1. Firefox version
2. Steps to reproduce
3. Expected vs actual behavior
4. Console error messages
5. Whether the same issue occurs in Chrome

## Automated Validation
The repository includes a validation script that checks:
- Manifest structure
- Required files
- Browser API polyfills
- Firefox-specific settings

Run it before manual testing:
```bash
cd /path/to/sabconnectplusplus
python3 validate_firefox.py
```

## Success Criteria
The extension is considered Firefox-compatible if:
- ✅ Loads without errors
- ✅ Popup displays correctly
- ✅ Settings page works
- ✅ Content scripts inject on supported sites
- ✅ Service worker runs without errors
- ✅ Storage persists between sessions
- ✅ No console errors under normal operation
- ✅ All validation checks pass

## Notes
- Temporary extensions in Firefox are removed on browser restart
- For permanent installation, the extension must be signed by Mozilla
- Firefox Developer Edition allows unsigned extensions with config changes
