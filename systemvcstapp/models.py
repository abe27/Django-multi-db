from django.db import models

# Create your models here.


class WhouseFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True,
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "WHOUSE"
        app_label = "systemvcstapp"
        verbose_name = "ข้อมูลคลังสินค้า"
        verbose_name_plural = "คลังสินค้า"


class CorpFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True,
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=50, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=255, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2', null=False, blank=True)
    FCADDR1 = models.CharField(
        max_length=50, db_column='FCADDR1', verbose_name="FCADDR1", null=False, blank=True)
    FCADDR12 = models.CharField(
        max_length=50, db_column='FCADDR12', verbose_name="FCADDR12", null=False, blank=True)
    FCADDR2 = models.CharField(
        max_length=50, db_column='FCADDR2', verbose_name="FCADDR2", null=False, blank=True)
    FCADDR2 = models.CharField(
        max_length=50, db_column='FCADDR22', verbose_name="FCADDR22", null=False, blank=True)
    FCTEL = models.CharField(
        max_length=50, db_column='FCTEL', verbose_name="FCTEL", null=False, blank=True)
    FCFAX = models.CharField(
        max_length=50, db_column='FCFAX', verbose_name="FCFAX", null=False, blank=True)
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)
    FCTAXID = models.CharField(
        max_length=50, db_column='FCTAXID', verbose_name="FCTAXID", null=False, blank=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "CORP"
        app_label = "systemvcstapp"
        verbose_name = "รายชื่อบริษัท"
        verbose_name_plural = "รายชื่อบริษัท"


class ProductTypeFormulaVCST(models.Model):
    FCSKID = models.CharField(
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        primary_key=True,
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "PRODTYPE"
        app_label = "systemvcstapp"
        verbose_name = "ประเภทสินค้า"
        verbose_name_plural = "ประเภทสินค้า"


class UmFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True,
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "UM"
        app_label = "systemvcstapp"
        verbose_name = "ข้อมูลหน่วยสินค้า"
        verbose_name_plural = "หน่วยสินค้า"


class PdGrdFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True,
        max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="ข้อมูลเพิ่มเติม", db_column='FCNAME2')
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCNAME

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "PDGRP"
        app_label = "systemvcstapp"
        verbose_name = "ข้อมูลกลุ่ม"
        verbose_name_plural = "กลุ่มสินค้า"


class ProductFormulaVCST(models.Model):
    FCSKID = models.CharField(
        primary_key=True, max_length=8, verbose_name="ID", db_column='FCSKID', editable=False)
    FCCODE = models.CharField(
        max_length=20, verbose_name="รหัส", db_column='FCCODE')
    FCNAME = models.CharField(
        max_length=20, verbose_name="ชื่อ", db_column='FCNAME')
    FCNAME2 = models.CharField(
        max_length=20, verbose_name="เพิ่มเติม1", db_column='FCNAME2')
    FCSNAME = models.CharField(
        max_length=20, verbose_name="เพิ่มเติม2", db_column='FCSNAME')
    FCSNAME2 = models.CharField(
        max_length=20, verbose_name="เพิ่มเติม3", db_column='FCSNAME2')
    FCDATASER = models.CharField(
        max_length=20, verbose_name="รหัสจำเพราะ", db_column='FCDATASER', editable=False)
    FCCORP = models.ForeignKey(
        CorpFormulaVCST, verbose_name="ชื่อบริษัท", db_column='FCCORP', on_delete=models.CASCADE)
    FCTYPE = models.ForeignKey(
        ProductTypeFormulaVCST, verbose_name="ประเภท", db_column='FCTYPE', on_delete=models.CASCADE)
    FCPDGRP = models.ForeignKey(
        PdGrdFormulaVCST, verbose_name="กลุ่ม", db_column='FCPDGRP', on_delete=models.CASCADE)
    FCUM = models.ForeignKey(
        UmFormulaVCST, verbose_name="หน่วย", db_column='FCUM', on_delete=models.CASCADE)
    FTDATETIME = models.DateTimeField(
        verbose_name="สร้างเมื่อ", db_column='FTDATETIME', auto_now_add=True)
    FTLASTEDIT = models.DateTimeField(
        verbose_name="แก้ไขเมื่อ", db_column='FTLASTEDIT', auto_now=True)
    FTLASTUPD = models.DateTimeField(
        verbose_name="อัพเดทเมื่อ", db_column='FTLASTUPD', auto_now=True)

    def __str__(self) -> str:
        return self.FCSKID

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "PROD"
        app_label = "systemvcstapp"
        verbose_name = "รายการข้อมูลสินค้า"
        verbose_name_plural = "รายการสินค้า"
