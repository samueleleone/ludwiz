import discord
import utilites

async def send_weapon_details(ctx,weapon,content_onBook):
    if (content_onBook):
        for tupla in content_onBook:
            embed = discord.Embed(title=weapon.capitalize(), color=0x66ff66)
            for column, value in tupla.items():
                if (column == "Nome"):
                    embed.title = value
                embed = embed.add_field(name=column, value=value, inline=True)
            await ctx.send(embed=embed)

    else:
        await ctx.send("```Non trovo l'arma [" + weapon.capitalize() + "]```")


async def send_weapons_list(ctx,category,bookContent):
  if(bookContent):
            embed = discord.Embed(title=category.capitalize(), color=0x66ff66)
            embed_second = discord.Embed(title=category.capitalize(), color=0x66ff66)
            embed_third = discord.Embed(title=category.capitalize(), color=0x66ff66)
            i=0
            flag=0
            for tupla in bookContent:
                for column,value in tupla.items():
                    if(column != "Categoria"):
                        if(i<24):
                            embed.add_field(name=column,value=value)
                            i=i+1
                        elif(i<48):
                                flag=1
                                embed_second.add_field(name=column, value=value)
                                i = i + 1
                        elif(i<96):
                                flag=2
                                embed_third.add_field(name=column,value=value)
                                i=i+1
                    else:
                        embed.title=value
                        embed_second.title=value
                        embed_third.title=value
            await ctx.send(embed=embed)
            if(flag==1):
                await ctx.send(embed=embed_second)
            if(flag==2):
                await ctx.send(embed=embed_second)
                await ctx.send(embed=embed_third)

  else:
            await ctx.send("```Non trovo le armi di categoria [" + category.capitalize() + "]```")