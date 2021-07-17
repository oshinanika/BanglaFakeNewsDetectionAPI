using System;
using BanglaFakeNewsDetectionApp.Areas.Identity.Data;
using BanglaFakeNewsDetectionApp.Data;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.UI;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

[assembly: HostingStartup(typeof(BanglaFakeNewsDetectionApp.Areas.Identity.IdentityHostingStartup))]
namespace BanglaFakeNewsDetectionApp.Areas.Identity
{
    public class IdentityHostingStartup : IHostingStartup
    {
        public void Configure(IWebHostBuilder builder)
        {
            builder.ConfigureServices((context, services) => {
                services.AddDbContext<AppDbContext>(options =>
                    options.UseSqlServer(
                        context.Configuration.GetConnectionString("AppDbContextConnection")));

                    //services.AddDefaultIdentity<IdentityUser>(options => options.SignIn.RequireConfirmedAccount = true)
                    //   .AddEntityFrameworkStores<AppDbContext>();
                
                services.AddDefaultIdentity<ApplicationUser>(options => {
                    options.Password.RequireLowercase = false;
                    options.Password.RequireUppercase = false;
                    options.SignIn.RequireConfirmedAccount = false;
                })
                    .AddEntityFrameworkStores<AppDbContext>();
            });

        }
    }
}