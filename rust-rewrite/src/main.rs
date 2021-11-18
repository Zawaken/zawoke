mod commands;
use serenity::async_trait;
use serenity::client::{Client, Context, EventHandler};
use serenity::model::{
    channel::Message,
    gateway::Ready,
    prelude::{Activity, OnlineStatus, ReactionType}
};
use serenity::framework::standard::{
    StandardFramework,
    macros::{
        group
    }
};
use std::iter;
use commands::{
    fun::*,
    utilities::*,
};

#[group("Fun")]
#[commands(flip, roll)]
struct Fun;

#[group("Utilities")]
#[commands(ping)]
struct Utilities;



struct Handler;

#[async_trait]
impl EventHandler for Handler {
    async fn ready(&self, context: Context, ready: Ready) {
        let repeated: String = iter::repeat("-").take(20).collect();
        print!("{}[2J", 27 as char);
        println!("{}", repeated);
        println!("Logged in as");
        println!("{} - {}", ready.user.name, ready.user.id);
        println!("{} is currently running in {} servers", ready.user.name, ready.guilds.len());
        println!("{}", repeated);
        context.set_presence(Some(Activity::watching("anime")), OnlineStatus::Online).await;
    }
    async fn message(&self, ctx: Context, msg: Message) {
        if msg.content.contains("heck") {
            msg.react(&ctx.http, ReactionType::Unicode('🚫'.to_string())).await;
        }
    }
}

#[tokio::main]
async fn main() {
    let framework = StandardFramework::new()
        .configure(|c| c.prefix("a "))
        // .group(&GENERAL_GROUP)
        .group(&FUN_GROUP)
        .group(&UTILITIES_GROUP);

    //let token = env::var("TOKEN").expect("token");
    let mut client = Client::builder("")
    // let mut client = Client::builder(&token)
        .event_handler(Handler)
        .framework(framework)
        .await
        .expect("Error creating client");
    
    if let Err(why) = client.start().await {
        println!("An error occured while running the client: {:?}", why);
    }
}