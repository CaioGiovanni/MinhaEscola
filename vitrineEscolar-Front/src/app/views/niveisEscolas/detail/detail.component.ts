import { Component, OnInit } from '@angular/core';
import { SharedService} from 'src/app/shared.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {

  EscolaList:any=[];
  selectedSchool:any;

  constructor(private service:SharedService, private route: ActivatedRoute) { 
    this.route.params.subscribe(params => this.selectedSchool = params['id']);
  }

  ngOnInit(): void {
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
      this.selectedSchool = this.getSchool(this.selectedSchool);
    });
  }

  getSchool(pk: any) {
    return this.EscolaList?.results.find((escola: any) => escola.pk === parseInt(pk));
  }
}
