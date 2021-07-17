using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using API2PYTHON.Models;
using System.Net.Http;
using API2PYTHON.Interfaces;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System.Text;
using Microsoft.Extensions.Configuration;

namespace API2PYTHON.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class FakeNewsController : ControllerBase
    {
        #region private variables
        private readonly IConfiguration _config;
       // private readonly IUtilityApiCaller _apiCaller;
       // private readonly IUtilityImgconvertion _utilityImgProc;
        private readonly IApiUrlMngr _apiUrlMngr;
        //string ApiConnUrl = "http://192.168.20.192/PredictML/";
        string ApiConnUrl;


        public FakeNewsController(IApiUrlMngr apiUrlMngr, IConfiguration config)
        {
            _apiUrlMngr = apiUrlMngr;
            _config = config;

            ApiConnUrl = _config.GetValue<string>("PredictML");
        }

        // private readonly IUtilityLogs _logs;
        #endregion

        #region DetectFakeNews
        [HttpPost]
        [Route("DetectFakeNews")]
        [DisableRequestSizeLimit]
        //[Authorize(AuthenticationSchemes = "Bearer")]
        public async Task<IActionResult> GetFakeNewsPrediction(News newsContent)
        {
            StatusResult<string> status = new StatusResult<string>();

            try
            {
                //News news = new News();
                //news.news = newsContent;
                var data = JsonConvert.SerializeObject(newsContent);
                var content = new StringContent(data, Encoding.UTF8, "application/json");
                HttpClient client = new HttpClient();
 
               

                string endpoint = ApiConnUrl + "api/detectfakenews";
                
                HttpResponseMessage response = await client.PostAsync(endpoint, content);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                dynamic jToken = JToken.Parse(responseBody);
                var result = jToken.result;




                    status.Status = jToken.status;
                    status.Message = jToken.message;
                    status.Result = jToken.result;



                return Ok(status);

              }
            catch(Exception ex)
            {
                status.Status = "FAILED";
                status.Message = "Failed to get ";
                status.Result = ex.ToString();
            }
            return Ok(status);

        }

        #endregion

        #region DetectFakeNewswithEpoch
        [HttpPost]
        [Route("DetectFakeNewswithEpoch")]
        //[Authorize(AuthenticationSchemes = "Bearer")]
        public async Task<IActionResult> GetFakeNewsPredictionwithEpoch(NewsEpoch newsepoch)
        {
            StatusResult<string> status = new StatusResult<string>();

            try
            {
                //NewsEpoch newsepoch = new NewsEpoch();
                //newsepoch.news = news;
                //newsepoch.epoch = epoch;
                var data = JsonConvert.SerializeObject(newsepoch);
                var content = new StringContent(data, Encoding.UTF8, "application/json");
                HttpClient client = new HttpClient();
 
                

                string endpoint = ApiConnUrl + "api/detectfakenewsepoch";

                HttpResponseMessage response = await client.PostAsync(endpoint, content);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                dynamic jToken = JToken.Parse(responseBody);
                var result = jToken.result;

                status.Status = jToken.status;
                status.Message = jToken.message;
                status.Result = jToken.result;
                return Ok(status);

            }
            catch
            {
                status.Status = "FAILED";
                status.Message = "Failed to get result";
                status.Result = null;
            }
            return Ok(status);

        }

        #endregion


        #region GetModelAccuracy
        [HttpGet]
        [Route("GetModelAccuracy")]
        //[Authorize(AuthenticationSchemes = "Bearer")]
        public async Task<IActionResult> GetModelAccuracy()
        {
            StatusResult<string> status = new StatusResult<string>();

            try
            {


                HttpClient client = new HttpClient();

                string endpoint = ApiConnUrl + "/api/modelaccuracy";
                HttpResponseMessage response = await client.GetAsync(endpoint);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                dynamic jToken = JToken.Parse(responseBody);
                var result = jToken.result;


                status.Status = jToken.status;
                status.Message = jToken.message;
                status.Result = jToken.result;

                return Ok(status);

            }
            catch
            {
                status.Status = "FAILED";
                status.Message = "Failed to get result";
                status.Result = null;
            }
            return Ok(status);

        }

        #endregion

        #region GetNewsDomainList
        [HttpGet]
        [Route("GetNewsDomainList")]
        //[Authorize(AuthenticationSchemes = "Bearer")]
        public async Task<IActionResult> GetDomainList()
        {
            StatusResult<string> status = new StatusResult<string>();

            try
            {


                HttpClient client = new HttpClient();

                string endpoint = ApiConnUrl + "api/domainlist";
                HttpResponseMessage response = await client.GetAsync(endpoint);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                dynamic jToken = JToken.Parse(responseBody);
                var result = jToken.result;


                status.Status = jToken.status;
                status.Message = jToken.message;
                status.Result = jToken.result;

                return Ok(status);

            }
            catch
            {
                status.Status = "FAILED";
                status.Message = "Failed to get result";
                status.Result = null;
            }
            return Ok(status);

        }

        #endregion

        #region GetNewsCategoryList
        [HttpGet]
        [Route("GetNewsCategoryList")]
        //[Authorize(AuthenticationSchemes = "Bearer")]
        public async Task<IActionResult> GetNewsCategoryList()
        {
            StatusResult<string> status = new StatusResult<string>();

            try
            {

                HttpClient client = new HttpClient();

                string endpoint = ApiConnUrl + "api/categorylist";
                HttpResponseMessage response = await client.GetAsync(endpoint);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                dynamic jToken = JToken.Parse(responseBody);
                var result = jToken.result;


                status.Status = jToken.status;
                status.Message = jToken.message;
                status.Result = jToken.result;

                return Ok(status);

            }
            catch
            {
                status.Status = "FAILED";
                status.Message = "Failed to get result ";
                status.Result = null;
            }
            return Ok(status);

        }

        #endregion

        #region GetSampleTrueNewsSet
        [HttpGet]
        [Route("GetSampleTrueNewsSet")]
        //[Authorize(AuthenticationSchemes = "Bearer")]
        public async Task<IActionResult> GetSampleTrueNewsSet()
        {
            StatusResult<string> status = new StatusResult<string>();

           try
            {
                //NewsSet result = new NewsSet();

                HttpClient client = new HttpClient();

                string endpoint = ApiConnUrl + "api/sampletrueset";
                HttpResponseMessage response = await client.GetAsync(endpoint);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                dynamic jToken = JToken.Parse(responseBody);
                //var data =  jToken.result.articleID;
                //result.articleID = data;
                //result.category=jToken.result.category ;
                //result.content=jToken.result.content ;
                //result.date=jToken.result.date ;
                //result.domain=jToken.result.domain ;
                //result.headline=jToken.result.headline ;
                //result.label = jToken.result.label ;
         var result = jToken.result;


                status.Status = jToken.status;
                status.Message = jToken.message;
                status.Result = Convert.ToString(result);

                return Ok(status);

            }
            catch
            {
                status.Status = "FAILED";
                status.Message = "Failed to get result";
                status.Result = null;
            }
            return Ok(status);

        }

        #endregion
        #region GetSampleFakeNewsSet
        [HttpGet]
        [Route("GetSampleFakeNewsSet")]
        //[Authorize(AuthenticationSchemes = "Bearer")]
        public async Task<IActionResult> GetSampleFakeNewsSet()
        {
            StatusResult<string> status = new StatusResult<string>();

            try
            {
               // NewsSet result = new NewsSet();


                HttpClient client = new HttpClient();


                string endpoint = ApiConnUrl + "api/samplefakeset";
                HttpResponseMessage response = await client.GetAsync(endpoint);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                dynamic jToken = JToken.Parse(responseBody);
                var result = jToken.result;


                status.Status = jToken.status;
                status.Message = jToken.message;
                status.Result = Convert.ToString(result); ;

                return Ok(status);

            }
            catch
            {
                status.Status = "FAILED";
                status.Message = "Failed to get result";
                status.Result = null;
            }
            return Ok(status);

        }

        #endregion

       
    }


}