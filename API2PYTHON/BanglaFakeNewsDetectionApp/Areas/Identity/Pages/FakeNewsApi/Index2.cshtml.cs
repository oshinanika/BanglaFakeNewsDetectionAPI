using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using BanglaFakeNewsDetectionApp.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace BanglaFakeNewsDetectionApp.Areas.Identity.Pages.FakeNewsApi
{
    public class Index2Model : PageModel
    {
        private HttpClient _client;

        public Index2Model(HttpClient client)
        {
            _client = client;
        }


        [BindProperty]
        public NewsModel News { get; set; }
        public string heading { get; set; }
        public string result { get; set; }


        public string ReturnUrl { get; set; }

        [TempData]
        public string ErrorMessage { get; set; }


        public class NewsModel
        {
            [Required]

            public string newsCon { get; set; }
            [Required]

            public int epoch { get; set; }


        }
        public void OnGet()
        {
        }
        public async Task<IActionResult> OnPostAsync()
        {
            // string ApiConnUrl = "http://192.168.20.192/PredictML/";
            string ApiConnUrl = "http://192.168.20.192/BanFakeNewsAPI/";
            string endpoint = ApiConnUrl + "api/FakeNews/DetectFakeNewswithEpoch";
            //newsContent = Request.Form[nameof(newsContent)];

            //            var data = JsonConvert.SerializeObject(News.newsCon);
            //            var content = new StringContent(data, Encoding.UTF8, "application/json");
            //            

            //            HttpResponseMessage response = await _client.PostAsync(endpoint, content);
            //// response.EnsureSuccessStatusCode();
            //            string responseBody = await response.Content.ReadAsStringAsync();
            //            dynamic jToken = JToken.Parse(responseBody);
            //            result = Convert.ToString(jToken.result);

            //NewsText.news = 
            NewsEpoch newstextobj = new NewsEpoch();
            newstextobj.news = News.newsCon;
            newstextobj.epoch = News.epoch;
            var data = JsonConvert.SerializeObject(newstextobj);
            JObject jObject = JObject.Parse(data);

            var stringContent = new StringContent(jObject.ToString(), Encoding.UTF8, "application/json");

            HttpResponseMessage response = await _client.PostAsync(endpoint, stringContent);
            response.EnsureSuccessStatusCode();
            string responseBody = "";
            if (response.IsSuccessStatusCode)
            {
                responseBody = await response.Content.ReadAsStringAsync();

            }
            dynamic jToken = JToken.Parse(responseBody);
            result = Convert.ToString(jToken.result);
            heading = "Fake News Detection Predictions with Epoch";


            //status.Status = jToken.status;
            //status.Message = jToken.message;
            //status.Result = jToken.result;

            // If we got this far, something failed, redisplay form
            return Page();
        }
     }
}
