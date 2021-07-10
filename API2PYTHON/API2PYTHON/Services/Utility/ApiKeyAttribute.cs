using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace API2PYTHON.Services.Utility
{
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method)] //use this attributes before controller/method so that it requires  apikey
    public class ApiKeyAttribute : Attribute, IAsyncActionFilter   //this can be used to decorate our controller
    {
        private const string ApiKeyHeaderName = "ApiKey";
        public async Task OnActionExecutionAsync(ActionExecutingContext context, ActionExecutionDelegate next)
        {
            //before going to controller
            if(!context.HttpContext.Request.Headers.TryGetValue(ApiKeyHeaderName, out var potentialApiKey))  //request header theke astese
            {
                context.Result = new UnauthorizedResult();
                return;
            }
            var configuration = context.HttpContext.RequestServices.GetRequiredService<IConfiguration>(); //
            var apikey = configuration.GetValue<string>("ApiKey");

            if (!apikey.Equals(potentialApiKey))   //appsetting er apikey theke astese
            {
                context.Result = new UnauthorizedResult();
                return;
            }
            await next();
            //after
        }
    }
}
