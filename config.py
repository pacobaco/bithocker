import os

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')  # Set in env vars
SERVER_ID = 1234567890  # Your server ID
LOG_CHANNEL_ID = 1111111111  # #message-logs
CALL_CHANNEL_ID = 2222222222  # #call-recordings
USAGE_CHANNEL_ID = 3333333333  # #app-usage-logs
SPY_LOG_ID = 4444444444  # #spy-trap-logs
CONSENT_CHANNEL_ID = 5555555555  # #third-party-consent

APPROVED_THIRD_PARTIES = ['trusted-app-key']  # API keys for third parties