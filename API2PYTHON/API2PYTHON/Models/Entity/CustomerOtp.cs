using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace API2PYTHON.Models.Entity
{
    [Table("CUSTOMER_OTPS")]
    public class CustomerOtp
    {
        [Column("OTP_ID", Order = 0)]
        [Required]
        [MaxLength(10)]
        [Key]
        public int OtpId { get; set; }
        [Column("MOBILENO", Order = 1)]
        [MaxLength(20)]
        public string? MobileNo { get; set; } = string.Empty;
        [Column("EMAIL", Order = 2)]
        [MaxLength(50)]
        public string? Email { get; set; } = string.Empty;
        [Column("OTP_CODE_SMS", Order = 3)]
        [MaxLength(20)]
        public string? OtpCodeSms { get; set; } = string.Empty;
        [Column("OTP_CODE_EMAIL", Order = 4)]
        [MaxLength(20)]
        public string? OtpCodeEmail { get; set; } = string.Empty;
        [Column("SMS_SENT_AT", Order = 5)]
        [MaxLength(7)]
        // [DataType(DataType.Date)]
        public DateTime? SmsSentAt { get; set; }
        [Column("EMAIL_SENT_AT", Order = 6)]
        [MaxLength(7)]
        //[DataType(DataType.Date)]
        public DateTime? EmailSentAt { get; set; }
        [Column("OTP_EXPIRED_AT", Order = 7)]
        [MaxLength(7)]
        //[DataType(DataType.Date)]
        public DateTime OtpExpiredAt { get; set; }
        [Column("OTP_FAILED_COUNT", Order = 8)]
        [MaxLength(10)]
        public int OtpFailedCount { get; set; } = 0;
        [Column("OTP_VERIFIED_AT", Order = 9)]
        [MaxLength(7)]
        //[DataType(DataType.Date)]
        public DateTime? OtpVerifiedAt { get; set; }

    }
}