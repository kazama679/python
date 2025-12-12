from odoo import models, fields, api


class Exam(models.Model):
    _name = 'school.exam'
    _description = 'Exam'

    exam_date = fields.Date(string='Exam Date')
    subject = fields.Char(string='Subject')
    school_id = fields.Many2one('school.school', string='School')
    student_ids = fields.Many2many('school.student', string='Students')
    avg_score = fields.Float(string='Average Score',
                             compute='_compute_avg_score', store=True)

    @api.depends('student_ids', 'student_ids.score')
    def _compute_avg_score(self):
        for rec in self:
            scores = rec.student_ids.mapped('score')
            rec.avg_score = sum(scores) / len(scores) if scores else 0.0

    @api.model
    def create_school(self, name, location=None, start_date=None):
        return self.env['school.school'].create({'name': name, 'location': location, 'start_date': start_date})

    @api.model
    def create_student(self, name, age, school_id, score=None):
        return self.env['school.student'].create({'name': name, 'age': age, 'school_id': school_id, 'score': score})
