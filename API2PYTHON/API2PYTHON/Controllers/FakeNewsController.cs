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

namespace API2PYTHON.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class FakeNewsController : ControllerBase
    {
        #region private variables
       // private readonly IConfiguration _config;
       // private readonly IUtilityApiCaller _apiCaller;
       // private readonly IUtilityImgconvertion _utilityImgProc;
        private readonly IApiUrlMngr _apiUrlMngr;

        public FakeNewsController(IApiUrlMngr apiUrlMngr)
        {
            _apiUrlMngr = apiUrlMngr;
        }

        // private readonly IUtilityLogs _logs;
        #endregion

        #region Get Customer Photos New
        [HttpGet]
        [Route("GetFakeNewsPrediction")]
        //[Authorize(AuthenticationSchemes = "Bearer")]
        public async Task<IActionResult> GetFakeNewsPrediction()
        {
            StatusResult<string> status = new StatusResult<string>();
            //if (String.IsNullOrEmpty(trackingNo))
            //{
            //    status.Status = "FAILED";
            //    status.Message = "User trackingNo can't be empty.";
            //    status.Result = null;
            //    return BadRequest(status);
            //}
            try
            {


                HttpClient client = new HttpClient();
                //ApiUrlDetails apiUrlDetails = _apiUrlMngr.GetApiUrlDeatils("VERIFID_ML");
                string ApiConnUrl = "http://192.168.20.192/VerifIDML/";
                //string endpoint = apiUrlDetails.ApiConnUrl + "api/test2/" + trackingNo;
                string endpoint = ApiConnUrl + "api/test2";
                HttpResponseMessage response = await client.GetAsync(endpoint);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                dynamic jToken = JToken.Parse(responseBody);
                var result = jToken.result;


                status.Status = "OK";
                status.Message = "Got result";
                status.Result = result;

                return Ok(status);

              }
            catch
            {
                status.Status = "FAILED";
                status.Message = "Failed to get One of the photos, check error logs";
                status.Result = null;
            }
            return Ok(status);

        }

        #endregion
    }


}