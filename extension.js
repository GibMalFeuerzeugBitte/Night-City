const vscode = require('vscode');

// Cyberpunk Quotes Pool
const netrunnerQuotes = [
    "Wake the fuck up, Samurai. We have code to burn.",
    "In Night City, you can be anyone you want to be.",
    "Chrome is the future, meat is obsolete.",
    "The net is vast and infinite.",
    "Flatline detected. Reboot imminent.",
    "ICE breached. Access granted.",
    "Netrunner online. Neural link stable.",
    "Corporate firewall bypassed.",
    "Daemon uploaded successfully.",
    "Quickhack ready for deployment.",
    "Cyberdeck operating at maximum capacity.",
    "Welcome to the dark side of the net.",
    "Militech Systems: Armed and Operational"
];

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    // Erstelle Status Bar Item mittig (Left mit niedriger Priorität)
    const militechItem = vscode.window.createStatusBarItem(
        vscode.StatusBarAlignment.Left,
        -999999 // Negative Priorität = weiter rechts, näher zur Mitte
    );
    
    // Setze den Text mit Icon
    militechItem.text = '$(shield) MILITECH';
    militechItem.tooltip = 'Click to receive transmission from Night City';
    militechItem.command = 'night-city.netrunnerQuote';
    
    // Registriere Command für Cyberpunk Quotes
    const quoteCommand = vscode.commands.registerCommand('night-city.netrunnerQuote', () => {
        const randomQuote = netrunnerQuotes[Math.floor(Math.random() * netrunnerQuotes.length)];
        vscode.window.showInformationMessage(`🌃 ${randomQuote}`);
    });
    
    // Zeige das Item
    militechItem.show();
    
    // Registriere für Cleanup
    context.subscriptions.push(militechItem);
    context.subscriptions.push(quoteCommand);
    
    console.log('MILITECH Status Bar active - Night City Theme loaded');
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
