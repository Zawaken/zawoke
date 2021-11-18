use serenity::client::{Context};
use serenity::model::{
    channel::Message,
    prelude::{ReactionType}
};
use serenity::framework::standard::{
    CommandResult,
    macros::{
        command,
    }
};
use rand::Rng;
use rand::SeedableRng;
use rand::rngs::StdRng;

#[command]
async fn flip(ctx: &Context, msg: &Message) -> CommandResult {
    // let mut rng = rand::thread_rng();
    // let mut rng = StdRng::seed_from_u64(10);
    let mut rng = StdRng::from_entropy();
    let flip = rng.gen_range(0..2);
    // println!("debug flip: {}", flip);
    if flip == 0 {
        msg.react(&ctx.http, ReactionType::Unicode('⚪'.to_string())).await?;
    } else if flip == 1 {
        msg.react(&ctx.http, ReactionType::Unicode('⚫'.to_string())).await?;
    } else {
        println!("flip does not equal 1 or 0:  {}", flip);
    }

    Ok(())
}

#[command]
async fn roll(ctx: &Context, msg: &Message) -> CommandResult {
    // let mut roll: Message = msg.channel_id.send_message(ctx, |m| m.content("{} rolls {}")).await?;
    let droll = rand::thread_rng().gen_range(0..101);
    let format = format!("{} rolls {}", msg.author, droll);
    println!("Roll: {}", droll);
    // roll;
    msg.channel_id.say(ctx, format).await?;

    Ok(())
}