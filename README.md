# discord-scheduler-bot
Discord Scheduler Bot helps leaders schedule a custom alert message to inform players when it is their turn to perform some action. 

*Usage:* `!setup [interval] [interval-units] "[message]" [member-order-list]`

For example, a leader might want a list of players to choose their loot based on number of stars, one per 6 hour interval. He wants the message to read "@exampleuser Time to pick your loot! You have 6 hours!"

*Example Usage:* `!setup 6 hours "Time to pick your loot! You have 6 hours!" @exampleuser1 @exampleuser2 @exampleuser3`
