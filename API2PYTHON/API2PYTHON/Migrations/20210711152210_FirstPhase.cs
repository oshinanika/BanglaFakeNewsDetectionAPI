using System;
using Microsoft.EntityFrameworkCore.Migrations;

namespace API2PYTHON.Migrations
{
    public partial class FirstPhase : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "CUSTOMER_OTPS",
                columns: table => new
                {
                    OTP_ID = table.Column<int>(maxLength: 10, nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    MOBILENO = table.Column<string>(maxLength: 20, nullable: true),
                    EMAIL = table.Column<string>(maxLength: 50, nullable: true),
                    OTP_CODE_SMS = table.Column<string>(maxLength: 20, nullable: true),
                    OTP_CODE_EMAIL = table.Column<string>(maxLength: 20, nullable: true),
                    SMS_SENT_AT = table.Column<DateTime>(maxLength: 7, nullable: true),
                    EMAIL_SENT_AT = table.Column<DateTime>(maxLength: 7, nullable: true),
                    OTP_EXPIRED_AT = table.Column<DateTime>(maxLength: 7, nullable: false),
                    OTP_FAILED_COUNT = table.Column<int>(maxLength: 10, nullable: false),
                    OTP_VERIFIED_AT = table.Column<DateTime>(maxLength: 7, nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_CUSTOMER_OTPS", x => x.OTP_ID);
                });

            migrationBuilder.CreateTable(
                name: "CUSTOMER_PROFILES",
                columns: table => new
                {
                    TRACKING_NO = table.Column<int>(nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    MOBILENO = table.Column<string>(maxLength: 20, nullable: true),
                    EMAIL = table.Column<string>(maxLength: 100, nullable: true),
                    FULLNAMEEN = table.Column<string>(maxLength: 100, nullable: true),
                    OTPSMS = table.Column<string>(maxLength: 20, nullable: true),
                    OTPEMAIL = table.Column<string>(maxLength: 20, nullable: true),
                    NAME_OF_ORG = table.Column<string>(maxLength: 105, nullable: true),
                    MAKEDT = table.Column<DateTime>(nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_CUSTOMER_PROFILES", x => x.TRACKING_NO);
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "CUSTOMER_OTPS");

            migrationBuilder.DropTable(
                name: "CUSTOMER_PROFILES");
        }
    }
}
