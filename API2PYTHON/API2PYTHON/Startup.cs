using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using API2PYTHON.Interfaces;
using API2PYTHON.Managers;
using API2PYTHON.Models.Context;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.HttpsPolicy;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.OpenApi.Models;

namespace API2PYTHON
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {//-------------Database------------------

            services.AddDbContext<AppDBContext>(options =>
                                                        options.UseSqlServer(
                                                        Configuration.GetConnectionString("DefaultConnection")));


            services.AddScoped<IApiUrlMngr, ApiUrlMngr>();


            services.AddLogging();
            services.AddMvcCore(options => options.EnableEndpointRouting = false).AddAuthorization().AddNewtonsoftJson();

            services.AddControllers();
            services.AddCors(options =>
            {
                options.AddPolicy("CorsPolicy", builder => builder.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader().AllowCredentials().Build());
            });
            services.AddSwaggerGen(c =>
            {
                c.SwaggerDoc("v1", new OpenApiInfo
                {
                    Version = "v1",
                    Title = "Fake News Detection API",
                    Description = "In building applications, an API simplifies programming by abstracting the underlying implementation and only exposing objects or actions the developer needs. While a graphical interface for an email client might provide a user with a button that performs all the steps for fetching and highlighting new emails, an API for file input/output might give the developer a function that copies a file from one location to another without requiring that the developer understand the file system operations occurring behind the scenes.",
                    TermsOfService = new Uri("https://example.com/terms"),
                    Contact = new OpenApiContact
                    {
                        Name = "Anika Nahar",
                        Email = "anikanahar.cse@gmail.com",
                        Url = new Uri("https://example.com/license"),
                    },
                    License = new OpenApiLicense
                    {
                        Name = "Use with Permission from Anika Nahar",
                        Url = new Uri("https://example.com/license"),
                    }
                });
            });
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Error");
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            //app.UseDefaultFiles();
            //app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthorization();

            app.UseMvcWithDefaultRoute();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
            app.UseSwagger(c =>
            {
                //Change the path of the end point , should also update UI middle ware for this change                
                c.RouteTemplate = "/help/{documentName}/swagger.json";
            });

            // Enable middleware to serve swagger-ui (HTML, JS, CSS, etc.),
            // specifying the Swagger JSON endpoint.
            app.UseSwaggerUI(c =>
            {
                //c.IndexStream = () => GetType().Assembly.GetManifestResourceStream("TouchAntenna.Resources.SwaggerUI.index.html");
                c.RoutePrefix = "help";
                c.SwaggerEndpoint("v1/swagger.json", "Fake News Detection API");
                c.InjectStylesheet("../swagger-ui/custom.css");
                c.InjectJavascript("../swagger-ui/custom.js", "text/javascript");
                c.DocumentTitle = "Fake News Detection API";

            });
        }
    }
}
